PORT = 1337

build:
	jekyll build
run:
	jekyll serve --detach --port ${PORT} && firefox localhost:${PORT}
stop:
	kill -KILL `ps aux | grep jekyll | grep --invert-match grep | awk '{print $$2}'`
