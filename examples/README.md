# Example Projects

In this directory there are several collections of example projects which are intended as references for using the `cidipi` module.

## Usage

You can run the project with the command `python <filename>.py`, i.e:

```sh
python goto.py
```

By default, `cidipi` will start a process to run chrome. But, if you want to launch chrome separately, you have to set the environment variable `CHROME_REMOTE_URI` or the parameter `remote_uri` in the `Browser` class. Example:

```sh
# If you don't have Chrome on your device, you can launch Chrome using docker-compose.yml
export CHROME_REMOTE_URI=http://localhost:9222
python goto.py
```
