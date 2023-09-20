#!/bin/bash
diretorioTemporario=$(mktemp -d)
arquivosTemporarios=()

wc_count=0

executeEmSegundoPlano() {
	local diretorio="$1"
	local arquivo="$2"
	resultado=$(go run ./go/word_count.go "$diretorio")
	echo "$resultado" > "$arquivo"
}

for diretorio in "$1"/*; do
	arquivoTemporario=$(mktemp --tmpdir="$resultados")
	(executeEmSegundoPlano "$diretorio" "$arquivoTemporario")  &
	arquivosTemporarios+=("$arquivoTemporario")
done

wait

for arquivoTemporario in "${arquivosTemporarios[@]}"; do
	wc_count=$((wc_count + $(cat "$arquivoTemporario")))
	rm "$arquivoTemporario"
done

rmdir "$diretorioTemporario"

echo "$wc_count"

