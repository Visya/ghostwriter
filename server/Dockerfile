FROM continuumio/miniconda3:latest

WORKDIR /usr/src/app

COPY . .

RUN conda env create -f environment.yml
RUN echo "Wow"

EXPOSE 5000

CMD ["conda", "run", "--no-capture-output", "-n", "ghostwriter", "./entrypoint.sh"]
