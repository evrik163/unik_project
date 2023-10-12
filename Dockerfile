FROM postgres:11.5
USER postgres
ADD ./scripts/init.sql /docker-entrypoint-initdb.d/
COPY cool.py .
RUN python3 cool.py
RUN chown postgres:postgres /docker-entrypoint-initdb.d/init.sql
ENTRYPOINT ["docker-entrypoint.sh"]
EXPOSE 5432
CMD ["postgres"]
