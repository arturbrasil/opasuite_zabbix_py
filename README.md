# OPA SUITE + MONGODB + PYTHON

## Usuarios

> Contador de usuarios ativos

```js
$[?(@.status == "A")].length()
```

> Contador de usuarios online

```js
$[?(@.online == "on")].length()
```

> Contador de Atendimento por Usuários

```js
// macros
{#NOME} -> $.nome
{#ID} -> $._id.oid
// contador na 
$[?(@.id_atendente.oid == "{#ID_ATENDENTE}")].length()
```

> Contador de atendimentos por canal

```js
$[?(@.canal == "whatsapp")].length()
$[?(@.canal == "messenger")].length()
$[?(@.canal == "pabx")].length()
```

```js
$[?(@.canal == "whatsapp")].length()
$[?(@.id_atendente.oid == {#ID_ATENDENTE})].length()
```

```json

```
