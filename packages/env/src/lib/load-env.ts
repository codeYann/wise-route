import { dirname, join } from 'node:path'
import { fileURLToPath } from 'node:url'
import { config } from 'dotenv'
import { findWorkspaceRoot } from '@/lib/find-workspace-root.js'

export function loadEnv(envPath?: string) {
  const path =
    envPath ||
    join(findWorkspaceRoot(dirname(fileURLToPath(import.meta.url))), '.env')
  config({ path })
}
