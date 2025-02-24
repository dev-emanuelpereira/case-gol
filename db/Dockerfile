FROM bitnami/postgresql:17.4.0-debian-12-r2
ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=password
ENV POSTGRES_DB=case_gol
COPY case_gol.sql /docker-entrypoint-initdb.d/case_gol.sql