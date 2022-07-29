FROM python:3.10.5-alpine3.16

ENV PYTHONUNBUFFERED 1

WORKDIR /team_omega

COPY ./requirements.txt ./requirements.txt

COPY ./entry-point.sh ./entry-point.sh

RUN pip install --upgrade pip && \
    apk add --update --no-cache postgresql-client jpeg-dev && \
    apk add --update --no-cache --virtual .tmp-build-deps \
    build-base postgresql-dev musl-dev zlib zlib-dev linux-headers && \
    pip install -r requirements.txt

COPY . .

# ENV PATH="/scripts:/py/bin:$PATH"

CMD [ "./entry-point.sh" ]
