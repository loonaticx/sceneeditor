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

<table>
<tbody>
<tr class="odd">
<td><strong>Camera Control</strong></td>
<td></td>
<td><strong>Render Style</strong></td>
<td></td>
</tr>
<tr class="even">
<td>+</td>
<td>Zoom in</td>
<td>Shift + A</td>
<td>Show all</td>
</tr>
<tr class="odd">
<td>-</td>
<td>Zoom out</td>
<td>Control + F</td>
<td>Flash selected</td>
</tr>
<tr class="even">
<td>1</td>
<td>Front view (relative to render)</td>
<td>B</td>
<td>Toggle backface</td>
</tr>
<tr class="odd">
<td>2</td>
<td>Back view (relative to render)</td>
<td>L</td>
<td>Toggle lights</td>
</tr>
<tr class="even">
<td>3</td>
<td>Right view (relative to render)</td>
<td>T</td>
<td>Toggle texture</td>
</tr>
<tr class="odd">
<td><p>4 5 6</p></td>
<td><p>Left view (relative to render) Top view (relative to render) Bottom view (relative to render)</p></td>
<td><p>W</p>
<p><strong>Direct Controls</strong></p></td>
<td><p>Toggle wireframe</p></td>
</tr>
<tr class="even">
<td>7</td>
<td>¾ view (relative to render)</td>
<td>Delete</td>
<td>Delete selected object</td>
</tr>
<tr class="odd">
<td>8</td>
<td>Roll view about axis relative to camera's axis</td>
<td>Escape</td>
<td>Delete all</td>
</tr>
<tr class="even">
<td>9</td>
<td>Rotate around hot point</td>
<td>Page Down</td>
<td>Move down selected object's hierarchy</td>
</tr>
<tr class="odd">
<td>0</td>
<td>Rotate around hot point</td>
<td>Page Up</td>
<td>Move up selected object's hierarchy</td>
</tr>
<tr class="even">
<td>C</td>
<td>Center on hot point</td>
<td>Tab</td>
<td>Toggle widget mode</td>
</tr>
<tr class="odd">
<td>F</td>
<td>Fit on hot point</td>
<td>Shift + F</td>
<td>Grow widget to fit current window</td>
</tr>
<tr class="even">
<td>H</td>
<td>Move to (0,0,0)</td>
<td>I</td>
<td>Plant selected object at cursor intersection point</td>
</tr>
<tr class="odd">
<td>Shift + L</td>
<td>Toggle camera pivot point lock</td>
<td>M</td>
<td>Move widget in front of camera</td>
</tr>
<tr class="even">
<td>N</td>
<td>Select next possible camera COA (along last intersection ray)</td>
<td>P</td>
<td>Set active parent to selected object</td>
</tr>
<tr class="odd">
<td>U</td>
<td>Orbit upright camera about hot point</td>
<td>R</td>
<td>WRT reparent selected to active parent</td>
</tr>
<tr class="even">
<td>Shift + U</td>
<td>Upright camera</td>
<td>Shift + R</td>
<td>Reparent selected to active parent</td>
</tr>
<tr class="odd">
<td><p>` <strong>Undo/Redo</strong></p></td>
<td><p>Kill camera move task</p></td>
<td><p>S V Shift + V</p></td>
<td><p>Reselect last selected object Toggle widget visibility Toggle COA marker visibility</p></td>
</tr>
<tr class="even">
<td>[</td>
<td>Undo</td>
<td>&lt;</td>
<td>Shrink widget</td>
</tr>
<tr class="odd">
<td>]</td>
<td>Redo</td>
<td>&gt;</td>
<td>Expand widget</td>
</tr>
</tbody>
</table>


  [image]: doc/directtools2.jpg