public class AudioPlayer implements MediaPlayerInterface {
    private MediaAdapter mediaAdapter;

    public AudioPlayer() {
        this.mediaAdapter = new MediaAdapter();
    }

    @Override
    public void play(String audioType, String filename) {
        if (audioType.equalsIgnoreCase("mp3")) {
            mediaAdapter.play(audioType, filename);
        } else if(audioType.equalsIgnoreCase("mp4")) {
            System.out.println("Tocando arquivo MP4: " + audioType);
        } else {
            System.out.println("Formato não suportado: " + audioType);
        }
    }
}