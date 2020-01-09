FROM python:3
LABEL maintainer="Tu5k4rr@protonmail.com"
RUN mkdir /PastaBean
COPY ./PastaBean.py /PastaBean
WORKDIR /PastaBean
RUN pip install requests
CMD [ "python", "./PastaBean.py"]
