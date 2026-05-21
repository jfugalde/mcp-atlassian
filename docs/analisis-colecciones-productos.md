# Macross — colecciones y asignación de productos

Análisis y corrección aplicada vía `ryu-platform/tools/shopify-analysis/fix_macross_collections.py` (Shopify CLI `store execute --allow-mutations`).

**Estado tras fix (Admin API):**

| Colección | Productos |
|-----------|------------:|
| Oncológicos | 69 |
| Hematología (`hematologia-1`) | 25 |
| Reumatología | 12 |
| Infecciosas | 14 |
| Inmunológicos | 11 |
| Hormonales | 7 |
| Cardiología | 6 |
| Lo más vendido | 154 (inventario variante > 1, orden best selling) |

---

## Histórico del análisis

Análisis inicial basado en `catalog_export.json` (123 productos **ACTIVE**) y colecciones **publicadas** en `farmaciasmacross.com.mx` (mayo 2026).

---

## Cómo se asignan los productos hoy

| Colección (handle) | Productos en tienda | Mecanismo esperado |
|--------------------|----------------------:|--------------------|
| `medicamento-oncologicos-al-mejor-precio-alta-especialidad` | 66 | Colección inteligente por **tipo de producto** (+ muchos sin tipo) |
| `hematologia-1` | **0** | Reglas por tipo — **no coinciden o colección vacía** |
| `reumatologia-y-traumatologia` | 7 | Por tipo (reumatología / mixto) |
| `infecciosas-y-parasitarias` | 5 | Tipo = `Infecciosas y Parasitarias` |
| `medicamentos-para-el-sistema-inmunologico-1` | 10 | Inmunosupresor, antirretroviral, etc. |
| `productos-hormonales-especializados` | 5 | Hormonal / endocrino / “Especialidad” (parcial) |
| `cardiologia` | 4 | Tipo = `Cardiología` |
| `lo-mas-vendido` | 109 | Casi **todo el catálogo** (regla muy amplia o manual) |

Las colecciones inteligentes de Shopify usan el campo **Tipo de producto** (`productType` en Admin). El tema **no** asigna productos; solo enlaza a la colección.

---

## Problemas principales

### 1. `hematologia-1` está vacía (0 productos)

En catálogo hay **14+ productos** con tipos hematológicos, pero:

- Los de tipo `Oncológico y Hematológico` → solo en **Oncológicos** (6)
- `Hematológico y Reumatología` → **Reumatología** (2)
- **4× `Hematología` + 1× `Hematológico`** → **no están en ninguna colección de especialidad**

**Acción Admin:** Abrir colección **Hematología** (`hematologia-1`) → revisar reglas inteligentes. Deben incluir (cualquiera de estos tipos, modo OR):

- `Hematología`
- `Hematológico`
- `Oncológico y Hematológico`
- `Hematológico y Reumatología`

Guardar y comprobar que el contador de productos > 0.

### 2. 55 productos activos (45%) sin **Tipo de producto**

- **27** aparecen dentro de **Oncológicos** sin tipo (la colección los incluye por otra regla o inclusión manual).
- **19** solo en `lo-mas-vendido`, sin especialidad.
- **3** no aparecen en ninguna colección publicada.

**Acción Admin:** Completar **Tipo de producto** en cada ficha (alineado a la tabla de tipos abajo). Sin esto, las colecciones inteligentes fallan.

### 3. 29 productos activos fuera de todas las especialidades

| Tipo (conteo) | Ejemplo de problema |
|---------------|---------------------|
| (vacío) × 19 | Sin clasificación |
| `Hematología` × 4 | Deberían estar en `hematologia-1` |
| `Nefrología` / `Neurología` × 2 | No hay colección publicada |
| Otros × 4 | Reglas de hormonales / especialidad incompletas |

### 4. `lo-mas-vendido` incluye 109 de ~123 activos

No actúa como “top ventas” filtrado; funciona como **catálogo casi completo**. Aceptable si es intencional; si no, cambiar a regla manual o criterio de ventas en Admin.

### 5. Productos en varias especialidades (esperado)

8 productos con tipos mixtos (p. ej. `Oncológico y Hematológico`) pueden aparecer en más de una colección si las reglas OR lo permiten. Hoy solo están en **Oncológicos**.

---

## Tipos de producto en catálogo (18 valores, 123 activos)

| Conteo | Tipo de producto |
|-------:|------------------|
| 55 | *(vacío)* |
| 31 | Oncológico |
| 6 | Oncológico y Hematológico |
| 5 | Infecciosas y Parasitarias |
| 4 | Reumatología y Traumatología |
| 4 | Hematología |
| 3 | Inmunosupresor |
| 3 | Especialidad |
| 2 | Hematológico y Reumatología |
| 2 | Hematológico |
| 1 | Medicamentos para el sistema inmunológico |
| 1 | Antoconceptivo hormonal |
| 1 | Endocrinología |
| 1 | Nefrología y Urología |
| 1 | Nefrología |
| 1 | Antirretroviral |
| 1 | Neurología |
| 1 | Cardiología |

---

## Mapa recomendado tipo → colección

Usar estos **tipos exactos** en Admin (ortografía incluida) y reglas OR en cada colección inteligente:

| Colección | Tipos a incluir |
|-----------|-----------------|
| Oncológicos | `Oncológico`, `Oncológico y Hematológico` *(opcional: excluir si deben ir solo a hematología)* |
| Hematología (`hematologia-1`) | `Hematología`, `Hematológico`, `Oncológico y Hematológico`, `Hematológico y Reumatología` |
| Reumatología | `Reumatología y Traumatología`, `Hematológico y Reumatología` |
| Infecciosas | `Infecciosas y Parasitarias`, `Antirretroviral` |
| Inmunológicos | `Inmunosupresor`, `Medicamentos para el sistema inmunológico`, `Antirretroviral` *(si aplica)* |
| Hormonales | `Antoconceptivo hormonal`, `Endocrinología`, `Especialidad` *(revisar caso a caso)* |
| Cardiología | `Cardiología` |
| Lo más vendido | Manual o criterio ventas — **no** sustituye especialidad |

---

## Menú vs colecciones

- Menú `encabezado`: enlaces a colecciones (Admin → Navegación).
- Debe usar los mismos handles que el tema (`hematologia-1`, no `hematologia`).
- Ver `docs/runbook-iconos-categorias.md`.

---

## Verificación

```bash
# Conteos en tienda
for h in medicamento-oncologicos-al-mejor-precio-alta-especialidad hematologia-1 \
  reumatologia-y-traumatologia infecciosas-y-parasitarias \
  medicamentos-para-el-sistema-inmunologico-1 productos-hormonales-especializados \
  cardiologia lo-mas-vendido; do
  n=$(curl -sS "https://farmaciasmacross.com.mx/collections/$h/products.json?limit=250" \
    | python3 -c "import sys,json; print(len(json.load(sys.stdin).get('products',[])))")
  echo "$n  $h"
done

# Handles del tema vs tienda
python3 ryu-platform/tools/shopify-analysis/validate_macross_collections.py
```

**Objetivo saludable:** `hematologia-1` > 0; productos con tipo `Hematología` dentro de esa colección; vacíos de tipo < 10% del catálogo activo.
