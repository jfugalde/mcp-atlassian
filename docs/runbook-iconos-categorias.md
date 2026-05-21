# Runbook: iconos de categorías (Macross)

Guía para el equipo de tienda: cambiar iconos, títulos y orden de las especialidades **sin tocar código**.

---

## Requisito previo

En el editor de tema: **Configuración del tema → Icons → Enable Font Awesome icons** debe estar **activado**. Sin esto solo se verán los iconos SVG por defecto (no los de Font Awesome).

En la sección **Collection list** de la página de inicio: activar **Icon strip mode (replaces image tiles)**. Si está desactivado, verás tarjetas con foto de colección, no las pastillas con icono.

---

## No veo los iconos después de publicar

1. **Inicio** — baja hasta **“Explora por especialidad”**: debe verse una franja horizontal con pastillas (icono redondo + nombre). No está en el menú superior.
2. **/collections** — la cuadrícula de especialidades usa los mismos iconos; si la página se ve en blanco, publica de nuevo el tema (versión con `sf-collection-icons.css` actualizado).
3. **Solo cuadros de color sin dibujo** — Font Awesome no cargó (red, bloqueador, CDN). Revisa en el navegador que cargue `cdnjs.cloudflare.com/.../font-awesome/6.5.2/css/all.min.css`.
4. **Editor de tema** — el campo **Icon (Font Awesome classes)** está en cada **bloque** Collection dentro de **Collection list** o **Collections list page**, no en Configuración general sola.

Los iconos Font Awesome se muestran dentro de un **cuadrado redondeado tipo burbuja**, con colores suaves por especialidad (paleta Macross: azules, verdes, rosas, etc.). Las colecciones nuevas usan el tono azul gris por defecto hasta que desarrollo agregue su color en el tema (si hace falta un tono fijo).

---

## Colecciones reales (fuente de verdad)

Los enlaces, productos y conteos salen de **colecciones publicadas en Shopify**. El tema solo guarda el **handle** de cada colección.

**Handles válidos en tienda (8 colecciones publicadas):**

| Handle | Título en tienda |
|--------|------------------|
| `medicamento-oncologicos-al-mejor-precio-alta-especialidad` | Oncológicos |
| `hematologia-1` | Hematología (colección publicada; no usar `hematologia`) |
| `reumatologia-y-traumatologia` | Reumatología y traumatología |
| `infecciosas-y-parasitarias` | Infecciosas y Parasitarias |
| `medicamentos-para-el-sistema-inmunologico-1` | Inmunológicos |
| `productos-hormonales-especializados` | Hormonales |
| `cardiologia` | Cardiología |
| `lo-mas-vendido` | Lo más vendido (inteligente: inventario > 1; orden por más vendidos) |

**No usar** handles que no existen (dan 404), por ejemplo: `hematologia` (sin `-1`), `nefrologia`, `enfermedades-infecciosas-y-parasitarias`.

**Menú principal:** **Tienda online → Navegación → Menú `encabezado`**. Cada ítem debe apuntar al mismo handle que la colección real. Si cambias un handle en Admin, actualiza menú + bloques del tema.

**Validación / reparación (desarrollo):**

- `python3 ryu-platform/tools/shopify-analysis/validate_macross_collections.py`
- `python3 ryu-platform/tools/shopify-analysis/fix_macross_collections.py` (aplica reglas y tipos; requiere `shopify store auth`)

**Menú:** el menú **encabezado** (Especialidades → Hematología) apunta a `/collections/hematologia-1` y a la colección `gid://shopify/Collection/361956049063`. Si se revierte en Admin, volver a asignar esa colección publicada (no `hematologia`).

---

## Opción A — Editor de tema (recomendado)

Usar cuando quieres controlar la **página de inicio** y la página **/collections** con las mismas categorías seleccionadas.

1. **Tienda online → Personalizar**
2. **Página de inicio** → sección **Collection list** (“Explora por especialidad”)  
   **o** plantilla **Lista de colecciones** (`/collections`)
3. En el panel izquierdo, abre cada bloque **Collection** / **Collection item**
4. Campos útiles:
   - **Collection** — qué colección enlaza el bloque
   - **Title** — texto visible (opcional; si está vacío usa el título de la colección)
   - **Icon (Font Awesome classes)** — clases del icono, por ejemplo: `fa-solid fa-heart-pulse`
5. **Reordenar** categorías: arrastra los bloques en la lista del editor
6. **Agregar** categoría: *Agregar bloque* → Collection → elige colección e icono
7. **Quitar** categoría: elimina el bloque (no borra la colección en Admin)
8. **Guardar**

### Valores actuales de referencia (puedes copiar/pegar)

| Especialidad | Icono (campo Icon) |
|--------------|-------------------|
| Oncología | `fa-solid fa-ribbon` |
| Hematología | `fa-solid fa-droplet` |
| Reumatología y traumatología | `fa-solid fa-bone` |
| Infecciosas y parasitarias | `fa-solid fa-virus` |
| Sistema inmunológico | `fa-solid fa-shield-halved` |
| Hormonales | `fa-solid fa-flask` |
| Cardiología | `fa-solid fa-heart-pulse` |
| Lo más vendido | `fa-solid fa-star` |

Buscar más iconos: [fontawesome.com/icons](https://fontawesome.com/icons) — usar siempre el estilo **solid** (`fa-solid fa-…`).

---

## Opción B — Metafield en la colección

Usar cuando el icono debe ir **con la colección** en todo el sitio. **Obligatorio** si en `/collections` eliges **Select collections to show → All** (en ese modo no hay bloques del editor; solo metafield o SVG).

1. **Configuración → Datos personalizados → Colecciones**
2. Definición (una sola vez):
   - **Nombre:** Font Awesome icon  
   - **Namespace y clave:** `custom.fa_icon`  
   - **Tipo:** **Texto de una sola línea** (single line text)
3. **Productos → Colecciones** → abre una colección → metafield **Font Awesome icon**  
   Ejemplo: `fa-solid fa-lungs`
4. **Guardar**

### Prioridad (qué gana si hay dos valores)

1. Icono del **bloque en el editor de tema** (Opción A)  
2. Metafield **`custom.fa_icon`** en la colección (Opción B)  
3. Icono SVG por defecto del tema (solo si los dos anteriores están vacíos)

---

## Cambiar solo el orden

Solo en el **editor de tema** (Opción A): arrastra los bloques. No hace falta tocar metafields.

---

## Problemas frecuentes

| Síntoma | Qué revisar |
|---------|-------------|
| No aparece el icono FA, solo dibujo genérico | **Enable Font Awesome** en configuración del tema |
| Icono en blanco o cuadrado | Clase mal escrita; debe ser `fa-solid fa-nombre` (dos partes) |
| Cambié el metafield y no cambió en inicio | El bloque del editor tiene su propio campo **Icon** — vacíalo o actualízalo ahí |
| Nueva colección no sale en inicio | Agregar bloque en la sección Collection list y guardar |
| 404 al hacer clic en categoría | El handle del bloque no existe; usar tabla de handles válidos arriba |
| Menú y tarjetas no coinciden | Alinear menú `encabezado` con los mismos handles que los bloques del tema |
| `/collections` muestra todas las tiendas | En la sección, **Select collections to show** = **Selected** y define bloques |
| Sin burbuja de color en el icono | Revisar que FA esté activo; la burbuja solo aplica a iconos Font Awesome, no al SVG de respaldo |
| Colección nueva sin color de marca | Tono azul gris por defecto; pedir a desarrollo el color en tema si debe ser fijo |

---

## Rendimiento (resumen técnico)

Esta solución está pensada para ser **ligera** en la tienda:

| Qué | Impacto |
|-----|---------|
| Iconos | HTML + CSS en servidor (Liquid); **sin JavaScript** extra para dibujar iconos |
| Estilos `sf-collection-icons.css` | ~4 KB; solo en páginas con sección Collection list o lista `/collections` |
| Font Awesome (CDN) | ~40 KB (2 hojas CSS) en **todo el sitio** si “Enable Font Awesome” está activo; carga diferida (`media="print"` + `onload`) |
| Carrusel inicio (marquee) | Duplica ~8 pastillas en HTML para el bucle visual; coste bajo (16 enlaces, no miles) |
| `/collections` | `IntersectionObserver` solo para la animación de entrada; deja de observar al mostrarse |

**Recomendación:** Mantener el modo **Selected** con 8–12 categorías (como ahora), no listar cientos de colecciones con iconos FA. Si algún día se desactivan todos los iconos FA, se puede apagar **Enable Font Awesome** y el CDN deja de cargarse.

---

## Quién contactar para cambios de código

- Nuevas especialidades con SVG fijo por handle (fallback sin FA)  
- Cambios de diseño del carrusel / rejilla  
- Despliegue del tema desde Git  

Equipo técnico / desarrollo del tema **Farmacia_Macross**.

---

*Última actualización: burbujas por especialidad (`sf-collection-icons.css`), prioridad bloque → metafield → SVG, modo All solo con metafield.*
