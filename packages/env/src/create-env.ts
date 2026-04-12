import type * as z from 'zod'

export function createEnv<T extends z.ZodRawShape>(schema: z.ZodObject<T>) {
  const response = schema.safeParse(process.env)

  if (!response.success) {
    const issues = response.error.issues
      .map((e) => `  - ${e.path.join('.')}: ${e.message}`)
      .join('\n')
    throw new Error(`Invalid environment variables:\n${issues}`)
  }

  return response.data
}
