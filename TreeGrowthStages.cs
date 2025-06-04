using UnityEngine;
using UnityEngine.UI;
using System.Collections;

public class TreeGrowthStages : MonoBehaviour
{
    public RawImage treeDisplay; // Assign a UI RawImage in Canvas
    private Texture2D[] treeStages;
    private int currentStage = 0;
    public AudioSource bloomIntroAudio; // Assign your Bloom intro mp3 here

    void Start()
    {
        LoadTreeStages();
        StartCoroutine(PlayTreeStages());
    }

    void LoadTreeStages()
    {
        treeStages = new Texture2D[5];

        for (int i = 0; i < treeStages.Length; i++)
        {
            treeStages[i] = Resources.Load<Texture2D>("TreeStages/tree_stage_" + (i + 1));
            if (treeStages[i] == null)
            {
                Debug.LogError("Missing tree stage image at index: " + i);
            }
        }
    }

    IEnumerator PlayTreeStages()
    {
        while (currentStage < treeStages.Length)
        {
            treeDisplay.texture = treeStages[currentStage];
            currentStage++;
            yield return new WaitForSeconds(2f); // Change duration as needed
        }

        // After final stage, play Bloom's intro voice
        if (bloomIntroAudio != null)
        {
            bloomIntroAudio.Play();
        }
    }
}
