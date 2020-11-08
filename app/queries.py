from app.models import Commissions, Orders, OrderLines, ProductPromotions
from sqlalchemy.sql import func


def customers(session, date):
    """
    Method returns the number of distinct customers on a given date
    :param session: database connection session
    :param date: date string in YYYY-MM-DD format
    :return: number of distinct customer ids on a given day
    """
    return len(session.query(func.distinct(Orders.customer_id)).filter(Orders.created_at.contains(date)).all())


def aggregated_metrics(session, date):
    """
    :param session: database connection session
    :param date: date string in YYYY-MM-DD format
    :return: Method returns the number of sales, total sales amount, total discount on all orders, average discount rate
     and the average sale amount on a given date.
    """
    return session.query(
        Orders,
        func.sum(OrderLines.quantity),
        func.sum(OrderLines.total_amount),
        func.sum(OrderLines.full_price_amount) - func.sum(OrderLines.discounted_amount),
        func.avg(OrderLines.discount_rate),
        func.avg(OrderLines.total_amount)
    ).filter(Orders.created_at.contains(date)).join(OrderLines, Orders.id == OrderLines.order_id).first()


def commissions_order_average(session, date, total):
    """
    :param session: database connection session
    :param date: date string in YYYY-MM-DD format
    :param total: The total commissions on the specified date
    :return: returns the average commission paid per order on a given date
    """
    return (
            total /
            session.query(
                func.count(
                    func.distinct(Orders.id)
                )
            ).filter(
                Orders.created_at.contains(date)
            ).first()[0]
    )


def commission_by_promotion(session, date):
    """
    Function calculated the amount of commission generated by a promotion using a groupby sql expression. Method finds
    the promotions that are valid on the date provided.

    :param session: database connection session
    :param date: date string in YYYY-MM-DD format
    :return: Returns the amount of commission generated by each promotion on a given date.
    """
    return session.query(
        Orders,
        ProductPromotions.promotion_id,
        func.sum(Commissions.rate * OrderLines.total_amount)
    ).filter(
        Orders.created_at.contains(date),
        ProductPromotions.date.contains(date),
        Commissions.date.contains(date)
    ).join(
        OrderLines, OrderLines.order_id == Orders.id
    ).join(
        Commissions, Orders.vendor_id == Commissions.vendor_id
    ).join(
        ProductPromotions, ProductPromotions.product_id == OrderLines.product_id
    ).group_by(
        ProductPromotions.promotion_id
    ).all()


def total_commission(session, date):
    """
    :param session: database connection session
    :param date: date string in YYYY-MM-DD format
    :return: Returns the total commission earned across all promotions
    """
    return session.query(
        Orders,
        func.sum(OrderLines.total_amount * Commissions.rate)
    ).filter(
        Orders.created_at.contains(date),
        Commissions.date.contains(date)
    ).join(
        OrderLines, Orders.id == OrderLines.order_id
    ).join(
        Commissions, Commissions.vendor_id == Orders.vendor_id
    ).first()[1]


def get_data(session, date):
    """
    :param session: database connection session
    :param date: date string in YYYY-MM-DD format
    :return: Collates data across all queries into the desired format. This is then jsonified and returned the the
    endpoint user in app.routes.py
    """
    response = {}
    commissions_dict = {}
    _, total_items_sold, order_total, total_discount_amount, discount_rate_avg, order_total_avg = aggregated_metrics(
        session,
        date
    )
    response['customers'] = customers(session, date)
    response['total_items_sold'] = total_items_sold
    response['order_total'] = order_total
    response['total_discount_amount'] = total_discount_amount
    response['order_total_avg'] = order_total_avg
    response['discount_rate_avg'] = discount_rate_avg
    commissions_dict['promotions'] = {key: val for _, key, val in commission_by_promotion(session, date)}
    commissions_dict['total'] = total_commission(session, date)
    commissions_dict['order_average'] = commissions_order_average(session, date, commissions_dict['total'])
    response['commissions'] = commissions_dict
    return response
