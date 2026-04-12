import { dirname, join } from 'node:path'
import { fileURLToPath } from 'node:url'
import { config } from 'dotenv'
import type * as z from 'zod'
import { findWorkspaceRoot } from './lib/find-workspace-root.ts'

const __dirname = dirname(fileURLToPath(import.meta.url))
const workspaceRoot = findWorkspaceRoot(__dirname)

config({ path: join(workspaceRoot, '.env') })

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
