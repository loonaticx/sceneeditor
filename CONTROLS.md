# Enhanced Mouse Navigation

Enhanced mouse navigation is only available when 'Direct Tools' are
enabled. Information on enabling 'Direct Tools' is available in the
`Panda Tools <tools>` section.

Direct Tools gives more functionality to the middle mouse button. First,
clicking the middle mouse button changes the pivot point it uses to
rotate around the environment. The middle mouse button will also move
the camera depending on where the cursor is on the screen.

![image][]

|                                      |                                                |
|--------------------------------------|------------------------------------------------|
| Middle Mouse Click                   | Sets pivot point for rotating around the world |
| Middle Mouse + Middle Region         | Move camera parallel to ground                 |
| Shift + Middle Mouse + Middle Region | Move camera vertically                         |
| Middle Mouse + Edge Region           | Rotate camera around pivot point               |
| Middle Mouse + Corner Region         | Roll camera around pivot point                 |
| Shift + Middle Mouse + Edge Region   | Changes pitch of the camera                    |

The left mouse button is now used to select and manipulate objects in
the environment. Once an object is selected, it may be moved and
rotated.

|                                    |                                      |
|------------------------------------|--------------------------------------|
| Left Mouse Click                   | Select an object                     |
| Left Mouse + Middle Region         | Move object vertically               |
| Shift + Left Mouse + Middle Region | Move object parallel to ground       |
| Left Mouse + Edge Region           | Rotate object around its pivot point |
| Left Mouse + Corner Region         | Roll object around its pivot point   |
| Control + Left Mouse               | Rescale the model                    |

Direct Tools uses a large number of hot keys for camera control,
rendering styles, and object control. The full list is in the table
below.

+----------------+----------------+----------------+----------------+
| **Camera       |                | **Render       |                |
| Control**      |                | Style**        |                |
+----------------+----------------+----------------+----------------+
| \+             | Zoom in        | Shift + A      | Show all       |
+----------------+----------------+----------------+----------------+
| \-             | Zoom out       | Control + F    | Flash selected |
+----------------+----------------+----------------+----------------+
| 1              | Front view     | B              | Toggle         |
|                | (relative to   |                | backface       |
|                | render)        |                |                |
+----------------+----------------+----------------+----------------+
| 2              | Back view      | L              | Toggle lights  |
|                | (relative to   |                |                |
|                | render)        |                |                |
+----------------+----------------+----------------+----------------+
| 3              | Right view     | T              | Toggle texture |
|                | (relative to   |                |                |
|                | render)        |                |                |
+----------------+----------------+----------------+----------------+
| 4 5 6          | Left view      | W              | Toggle         |
|                | (relative to   |                | wireframe      |
|                | render) Top    | **Direct       |                |
|                | view (relative | Controls**     |                |
|                | to render)     |                |                |
|                | Bottom view    |                |                |
|                | (relative to   |                |                |
|                | render)        |                |                |
+----------------+----------------+----------------+----------------+
| 7              | ¾ view         | Delete         | Delete         |
|                | (relative to   |                | selected       |
|                | render)        |                | object         |
+----------------+----------------+----------------+----------------+
| 8              | Roll view      | Escape         | Delete all     |
|                | about axis     |                |                |
|                | relative to    |                |                |
|                | camera\'s axis |                |                |
+----------------+----------------+----------------+----------------+
| 9              | Rotate around  | Page Down      | Move down      |
|                | hot point      |                | selected       |
|                |                |                | object\'s      |
|                |                |                | hierarchy      |
+----------------+----------------+----------------+----------------+
| 0              | Rotate around  | Page Up        | Move up        |
|                | hot point      |                | selected       |
|                |                |                | object\'s      |
|                |                |                | hierarchy      |
+----------------+----------------+----------------+----------------+
| C              | Center on hot  | Tab            | Toggle widget  |
|                | point          |                | mode           |
+----------------+----------------+----------------+----------------+
| F              | Fit on hot     | Shift + F      | Grow widget to |
|                | point          |                | fit current    |
|                |                |                | window         |
+----------------+----------------+----------------+----------------+
| H              | Move to        | I              | Plant selected |
|                | (0,0,0)        |                | object at      |
|                |                |                | cursor         |
|                |                |                | intersection   |
|                |                |                | point          |
+----------------+----------------+----------------+----------------+
| Shift + L      | Toggle camera  | M              | Move widget in |
|                | pivot point    |                | front of       |
|                | lock           |                | camera         |
+----------------+----------------+----------------+----------------+
| N              | Select next    | P              | Set active     |
|                | possible       |                | parent to      |
|                | camera COA     |                | selected       |
|                | (along last    |                | object         |
|                | intersection   |                |                |
|                | ray)           |                |                |
+----------------+----------------+----------------+----------------+
| U              | Orbit upright  | R              | WRT reparent   |
|                | camera about   |                | selected to    |
|                | hot point      |                | active parent  |
+----------------+----------------+----------------+----------------+
| Shift + U      | Upright camera | Shift + R      | Reparent       |
|                |                |                | selected to    |
|                |                |                | active parent  |
+----------------+----------------+----------------+----------------+
| \`             | Kill camera    | S V Shift + V  | Reselect last  |
| **Undo/Redo**  | move task      |                | selected       |
|                |                |                | object Toggle  |
|                |                |                | widget         |
|                |                |                | visibility     |
|                |                |                | Toggle COA     |
|                |                |                | marker         |
|                |                |                | visibility     |
+----------------+----------------+----------------+----------------+
| \[             | Undo           | \<             | Shrink widget  |
+----------------+----------------+----------------+----------------+
| \]             | Redo           | \>             | Expand widget  |
+----------------+----------------+----------------+----------------+


  [image]: doc/directtools2.jpg