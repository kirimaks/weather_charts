CREATE TABLE IF NOT EXISTS charts(
    id      SERIAL PRIMARY KEY,
    name    VARCHAR(256)
);

CREATE TABLE IF NOT EXISTS data(
    id          BIGSERIAL PRIMARY KEY,
    chart_id    INTEGER REFERENCES charts(id),
    indicator   INTEGER NOT NULL
);
