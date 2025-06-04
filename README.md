✅ What You Need to Provide for the Unity Sakura Tree
C# Script File (Already done): 

You’ll provide the file named SakuraTreeGrowth.cs.

Audio File (You already have):

bloom_intro.mp3 (must be placed in Assets/Audio/)

Three Prefab Assets You Must Provide (or recreate via Unity):
These must be inside Assets/Prefabs/.

| Prefab Name            | Description                                          | Creation Option           |
| ---------------------- | ---------------------------------------------------- | ------------------------- |
| `TrunkSegment.prefab`  | A brown vertical cylinder (Unity primitive)          | Easy to create            |
| `BranchSegment.prefab` | A smaller brown tilted cylinder                      | Easy to create            |
| `Blossom.prefab`       | A small quad or sphere with pink transparent texture | Needs texture or material |

 **You Create Prefabs :**
 open Unity and:

Create a Cylinder and name it TrunkSegment.

Resize: Scale Y = 2.0, Color = brown

Drag it to Assets/Prefabs/ to make it a prefab.

Duplicate, resize, and rotate it to make BranchSegment.

Scale Y = 1.0, Rotate X = 30, Color = darker brown

For Blossom, create a small sphere or quad.

Assign a transparent pink material (like Sakura petals).

Name it Blossom and save to Assets/Prefabs/.

✅ Done! You now have all three prefabs.

** Folder Structure to Provide**

Assets/
├── Audio/
│   └── bloom_intro.mp3
├── Prefabs/
│   ├── TrunkSegment.prefab
│   ├── BranchSegment.prefab
│   └── Blossom.prefab
├── Scripts/
│   └── SakuraTreeGrowth.cs

**File 2: Fallback TreeGrowthStages.cs (using 5 images)** and Assets Folder that has all 5 images of tree with introduction voice of Bloom Tree.

**Final Step:**
links the script to a GameObject in the scene (like TreeController), it should run without errors.
Note: Support for different blossom colors (you can change one variable for pink/white/orange)


---

### ✅ Here is the highlighted section to **change blossom color**:

Inside `GrowTree()` (or `GrowBranches()`), look for this block:

```csharp
GameObject blossom = Instantiate(blossomPrefab, blossomPosition, Quaternion.identity);
blossom.transform.localScale = Vector3.one * 0.2f;

// 🌸 SET BLOSSOM COLOR HERE:
Renderer blossomRenderer = blossom.GetComponent<Renderer>();
if (blossomRenderer != null)
{
    blossomRenderer.material.color = new Color(1f, 0.7f, 0.9f); // Light pink
}
```

---

### 🎨 Recommended Colors:

| Sakura Theme      | RGB Values (Color)          | Line to Paste                 |
| ----------------- | --------------------------- | ----------------------------- |
| **Classic Pink**  | `new Color(1f, 0.7f, 0.9f)` | Default                       |
| **Pure White**    | `new Color(1f, 1f, 1f)`     | For white blossom             |
| **Autumn Orange** | `new Color(1f, 0.5f, 0.2f)` | For warm fall blossom         |
| **Calm Lavender** | `new Color(0.8f, 0.6f, 1f)` | For fantasy/dream environment |


## 🌸 Changing Blossom Color

To customize the Sakura blossom color, open `SakuraTreeGrowth.cs` and locate the line:

```csharp
blossomRenderer.material.color = new Color(1f, 0.7f, 0.9f); // Light pink
````

Replace the `new Color(...)` values with any of the following:

* Pink: `new Color(1f, 0.7f, 0.9f)`
* White: `new Color(1f, 1f, 1f)`
* Orange: `new Color(1f, 0.5f, 0.2f)`
* Lavender: `new Color(0.8f, 0.6f, 1f)`

**Make sure the `blossomPrefab` has a transparent shader to allow soft visuals.**

 
