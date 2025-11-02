from vercel.sandbox import AsyncSandbox as Sandbox
 
async def install_packages():
    sandbox = await Sandbox.create()
 
    cmd = await sandbox.run_command_detached('sudo', ['dnf', 'install', '-y', 'golang'])
    async for line in cmd.logs():
        print(line.data, end="")
 
    done = await cmd.wait()
    if done.exit_code != 0:
        raise SystemExit("dnf install failed")
 
    print("dnf install succeeded")
