import { existsSync } from 'node:fs'
import { join, resolve } from 'node:path'

export function findWorkspaceRoot(startDir: string) {
  let currentDir = resolve(startDir)
  while (true) {
    if (
      existsSync(join(currentDir, 'pnpm-workspace.yaml')) ||
      existsSync(join(currentDir, 'turbo.json'))
    ) {
      return currentDir
    }
    const parentDir = resolve(currentDir, '..')
    if (parentDir === currentDir) {
      return resolve(startDir)
    }
    currentDir = parentDir
  }
}
