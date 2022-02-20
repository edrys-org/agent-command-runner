async function run_command(command, timeout = 30000, host = "http://localhost", port = 8585, options = {}) {
    host = Edyrs.module.config.command_runner_host || host
    port = Edyrs.module.config.command_runner_port || port

    const abortController = new AbortController();
    const abortTimeout = setTimeout(() => abortController.abort(), timeout);
    
    const response = await fetch(`${host}:${port}/${encodeURIComponent(command)}`, {
        ...options,
        signal: abortController.signal
    });

    clearTimeout(abortTimeout)
    return await response.text()
}