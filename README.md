# Command Runner Agent

This is a simple python server than runs any commands sent to it over HTTP requests and returns the output in the response. It can be used to allow stations to run arbitrary commands on their host device by making requests to this server running locally.

## Usage

Install Python 3+, clone this repo, then run the server. By default the server runs on port `8585`.

```
python server.py 8585
```

To get the server to run a command, simply send the command as the GET path. For example:

```
GET localhost:8585/echo hello world
```

Will return the response:

```
hello world
```

We recommend URL-encoding the command before sending.

## Convenience JS library

While you can make requests from your module manually to the agent, we provide a convenience method that simplifies this further in `command-runner.js`.

```html
<script src="https://edrys-org.github.io/agent-command-runner/command-runner.js"></script>

<script>
    console.log(command_run('echo hello world')) // 'hello world'
</script> 
```