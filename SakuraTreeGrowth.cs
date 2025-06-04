using UnityEngine;

public class SakuraTreeGrowth : MonoBehaviour
{
    public GameObject trunkSegmentPrefab;
    public GameObject branchSegmentPrefab;
    public GameObject blossomPrefab;
    public AudioClip bloomIntro;

    public int trunkHeight = 5;
    public int branchesPerSegment = 2;
    public float growthInterval = 1.0f;

    private AudioSource audioSource;

    void Start()
    {
        audioSource = gameObject.AddComponent<AudioSource>();
        audioSource.clip = bloomIntro;
        audioSource.playOnAwake = false;

        StartCoroutine(GrowTree());
    }

    System.Collections.IEnumerator GrowTree()
    {
        Vector3 currentPosition = transform.position;

        // Grow the trunk
        for (int i = 0; i < trunkHeight; i++)
        {
            GameObject trunk = Instantiate(trunkSegmentPrefab, currentPosition, Quaternion.identity);
            trunk.transform.parent = transform;
            currentPosition += new Vector3(0, 1.0f, 0);
            yield return new WaitForSeconds(growthInterval);
        }

        // Add branches
        for (int i = 0; i < trunkHeight * branchesPerSegment; i++)
        {
            Vector3 branchPos = transform.position + new Vector3(
                Random.Range(-1f, 1f),
                Random.Range(1f, trunkHeight),
                Random.Range(-1f, 1f)
            );
            Quaternion rot = Quaternion.Euler(Random.Range(-30, 30), Random.Range(0, 360), 0);
            GameObject branch = Instantiate(branchSegmentPrefab, branchPos, rot);
            branch.transform.parent = transform;
            yield return new WaitForSeconds(0.2f);
        }

        // Add blossoms
        for (int i = 0; i < 100; i++)
        {
            Vector3 blossomPos = transform.position + new Vector3(
                Random.Range(-2f, 2f),
                Random.Range(1f, trunkHeight + 2),
                Random.Range(-2f, 2f)
            );
            GameObject blossom = Instantiate(blossomPrefab, blossomPos, Quaternion.identity);
            blossom.transform.parent = transform;
            yield return new WaitForSeconds(0.05f);
        }

        // Play Bloom's voice
        audioSource.Play();
    }
}
