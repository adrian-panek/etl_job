create table "market_data" (
  "id" serial primary key,
  "open" FLOAT not null,
  "close" FLOAT not null,
  "high" FLOAT not null,
  "low" FLOAT not null,
  "date" timestamp not null default NOW()
)