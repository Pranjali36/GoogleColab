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
 
