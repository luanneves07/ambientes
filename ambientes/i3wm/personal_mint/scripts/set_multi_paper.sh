#!/bin/bash

# Recupera lista de monitores conectados separando por x, + ou " " (Espaco) na seguinte ordem:
#
# |	$1	|	$2	|	$3	|	$4	|	$5	|
# 	NOME		STATUS		PRIMARIO	X		Y
#
# Caso nao seja o primario, a ordem sera:
# |	$1	|	$2	|	$3	|	$4	|	$5
# 	NOME		STATUS		X		Y		COMPLEMENTO

#MONITORS=$(xrandr --query |awk -F '[x+ ]' '{ ORS=";" } /\<connected\>/{print $1, $3, $4, $5}')
MONITORS="a;b;c;d;e;f;g;h;i;j;k;l;m;n;o"
IFS=';' read -ra SCREEN_LIST <<< "$MONITORS"

for idx in "${SCREEN_LIST[@]}"; do
	#TELA="${SCREEN_LIST[$idx]}"
	echo "${SCREEN_LIST[$idx]}"
done
