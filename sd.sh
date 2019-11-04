#!/usr/bin/bash
echo "1. Un programa sencillo con la definición de una variable."
./csc.py -ast tests/003_one_variable.cs
echo "####################################"

echo "2. Un programa sencillo con la definición de una constante."
./csc.py -ast tests/004_one_const.cs
echo "####################################"

echo "3. Un programa sencillo con un ciclo y una condicional."
./csc.py -ast tests/007_loop_conditional.cs
echo "####################################"

echo "4. Un programa con todas las instrucciones definidas."
./csc.py -ast tests/009_every_instruction.cs
echo "####################################"

echo "1. Un programa sencillo con la definición de una variable en el lugar incorrecto y en el orden incorrecto."
./csc.py -ast tests/010_incorrect_variable.cs
echo "####################################"

echo "2. Un programa sencillo que utiliza una cadena, variable y constante en un lugar que no está permitido."
./csc.py -ast tests/011_incorrect_string.cs
echo "####################################"

echo "3. Un programa sencillo con un ciclo definido pero usando una gramática incorrecta."
./csc.py -ast tests/012_incorrect_loop.cs
echo "####################################"