from flask import Flask, request, render_template, url_for

app = Flask(__name__)


@app.route('/gallery', methods=['POST', 'GET'])
def return_carousel():
    pic_count = 5
    if request.method == 'POST' and request.files['file']:
        while True:
            try:
                open(f'static/img/{pic_count}.jpg')
                pic_count += 1
            except FileNotFoundError:
                print(pic_count)
                request.files['file'].save(f'static/img/{pic_count}.jpg')
                break
    pictures = [(f"{url_for('static', filename=f'img/{j}.jpg')}", f"mars_{pic_count}")
                for j in range(1, pic_count + 1)]
    return render_template('carousel.html', pictures=pictures)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')