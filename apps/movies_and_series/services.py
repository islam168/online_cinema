from apps.users.models import Subscription
from datetime import datetime, timedelta, date
from django.db.models import Avg


def get_content(user, purchase, user_date_of_birth, age_rat, obj):
    release_date = obj.release_date
    try:
        content = obj.content.url
    except ValueError:
        content = ''
    today = date.today()
    user_age = today.year - user_date_of_birth.year
    if today.month < user_date_of_birth.month or (today.month == user_date_of_birth.month
                                                  and today.day < user_date_of_birth.day):
        user_age -= 1

    if user_age < age_rat:
        return 'Контент не доступен, вам недостаточно лет'
    else:
        if purchase is not None:
            purchase = str(purchase)
            purchase_date = purchase.split('Дата покупки: ')[1]
            dt = datetime.strptime(purchase_date, '%Y-%m-%d')
            subs_title = purchase.split('Подписка: ')[1].split(',')[0]
            subs = str(Subscription.objects.filter(title=subs_title).first())
            duration = str(subs.split('Длительность: ')[1])
            result = (dt + timedelta(days=int(duration))).strftime('%Y-%m-%d')
            if purchase_date > result:
                return f'Пожалуйста обновите свою подписку, дата оформления вашей подписки {purchase_date}. ' \
                       f'Срок окончания был {result}'
            else:
                subs_day = subs.split('контента: ')[1].split(',')[0]
                day = (release_date + timedelta(days=int(subs_day))).strftime('%Y-%m-%d')
                today = today.strftime('%Y-%m-%d')
                if today >= day:
                    if content == '':
                        return 'Контент ещё не вышел'
                    return f'http://127.0.0.1:8000{content}'
                else:
                    difference = (datetime.strptime(day, "%Y-%m-%d").date() -
                                  datetime.strptime(today, "%Y-%m-%d").date()).days
                    return f'Контент будет доступен через {difference} день'

        else:
            return 'Пожалуйста купите подписку'


