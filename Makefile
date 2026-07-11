.PHONY: serve build clean

serve:
	exec hugo server -D --bind 0.0.0.0 --port 1313 --baseURL / --disableFastRender

build:
	hugo --minify --baseURL https://marcello1099.github.io/servi-mariae/

clean:
	rm -rf public resources .hugo_build.lock