#!/usr/bin/env sh

set -o errexit
set -o pipefail
set -o nounset

case "$1" in
    image/*)
        ueberzug layer --parser bash < <(
            printf '{"action": "add", "identifier": "preview", "x": %s, "y": %s, "width": %s, "height": %s, "path": "%s"}\n' \
            "$2" "$3" "$4" "$5" "$1"
        )
        exit 0;;
    *)
        exit 1;;
esac

