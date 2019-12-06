#!/bin/bash

source stock_env/bin/activate

pip install -r requirements.txt

python search_tt.py "mercado de ações" mercadoacoes
python search_tt.py "ibovespa" ibovespa
python search_tt.py "ações em alta" acoesalta
python search_tt.py "ações em baixa" acoesbaixa
python search_tt.py "mercado financeiro" mercadofinanceiro
python search_tt.py "bolsa de valores" bolsavalores
python search_tt.py "bolsa em alta" bolsaalta
python search_tt.py "bolsa em baixa" bolsabaixa
python search_tt.py "risco brasil" riscopais
python search_tt.py "dívida publica" dividapublica



local=$(pwd)

pathzao="${local}/output"

files=$(ls ${pathzao})

for i in $files 
do 
    aws s3 cp "${pathzao}/${i}" "s3://stockmaurofs/output/${i}" 
    rm "${pathzao}/${i}" 
done
