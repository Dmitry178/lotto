FROM python:3.10-slim
COPY ./main.py ./main.py
COPY ./bag.py ./bag.py
COPY ./card.py ./card.py
COPY ./game.py ./game.py
COPY ./player.py ./player.py
CMD python ./main.py
