from apps.users.models import Subscription
from datetime import datetime, timedelta


def get_content(user, purchase, obj):
    release_date = obj.release_date
    content = obj.content.url
    if purchase is not None:
        purchase = str(purchase)
        purchase_date = purchase.split('Дата покупки: ')[1]
        dt = datetime.strptime(purchase_date, '%Y-%m-%d')
        result = (dt + timedelta(days=30)).strftime('%Y-%m-%d')
        if purchase_date > result:
            return f'Пожалуйста обновите свою подписку, дата оформления вашей подписки {purchase_date}. ' \
                   f'Срок окончания был {result}'
        else:
            subs_title = purchase.split('Подписка: ')[1].split(',')[0]
            subs = str(Subscription.objects.filter(title=subs_title).first())
            subs_day = subs.split('контента: ')[1]
            day = (release_date + timedelta(days=int(subs_day))).strftime('%Y-%m-%d')
            today = datetime.today().strftime('%Y-%m-%d')
            if today >= day:
                return f'http://127.0.0.1:8000{content}'
            else:
                difference = (datetime.strptime(day, "%Y-%m-%d").date() -
                              datetime.strptime(today, "%Y-%m-%d").date()).days
                return f'Эпизод будет доступен через {difference} день'

    else:
        return 'Пожалуйста купите подписку'

