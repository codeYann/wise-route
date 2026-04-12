import * as z from 'zod'

const apiBaseSchema = z.object({
  NODE_ENV: z
    .enum(['development', 'production', 'test', 'staging'])
    .default('development'),
})

const databaseSchema = z.object({
  PG_USER: z.string().nonempty('PG_USER is required'),
  PG_PASSWORD: z.string().nonempty('PG_PASSWORD is required'),
  PG_DB: z.string().nonempty('PG_DB is required'),
  PG_PORT: z.string().default('5432').transform(Number),
})

const redisSchema = z.object({
  REDIS_PASSWORD: z.string().nonempty('REDIS_PASSWORD is required'),
})

const rabbitmqSchema = z.object({
  RABBITMQ_USER: z.string().nonempty('RABBITMQ_USER is required'),
  RABBITMQ_PASSWORD: z.string().nonempty('RABBITMQ_PASSWORD is required'),
  RABBITMQ_PORT: z.string().default('5672').transform(Number),
  RABBITMQ_MANAGEMENT_PORT: z.string().default('15672').transform(Number),
})

export const api = {
  schema: () =>
    z.object({
      ...apiBaseSchema.shape,
      ...databaseSchema.shape,
      ...redisSchema.shape,
      ...rabbitmqSchema.shape,
    }),
}
