# OPA SUITE + MONGODB + PYTHON

## A

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
