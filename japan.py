from datetime import datetime
import pytz

from flask import Flask
from flask.templating import render_template
from api import get_weather

app = Flask(__name__)


@app.route('/')
def hello_world():
    is_japan = datetime(year=2015, month=5, day=24) <= datetime.today() <= datetime(year=2015, month=6, day=6)

    days_left = datetime(year=2015, month=5, day=24) - datetime.today()

    japan_time = datetime.now(tz=pytz.timezone('Asia/Tokyo')).strftime('%B %-d, %H:%M')

    weather = {
        'tokyo': get_weather(35.673343, 139.710388),
        'kyoto': get_weather(35.0061, 135.76095),
    }

    ctx = {
        'is_japan': is_japan,
        'weather': weather,
        'days_left': days_left.days,
        'japan_time': japan_time
    }

    return render_template('main.html', context=ctx)


if __name__ == '__main__':
    app.run(debug=True)
