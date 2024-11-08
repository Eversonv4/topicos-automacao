public class MediaAdapter implements MediaPlayerInterface {
    private OldMediaPlayerInterface oldMediaPlayer;

    public MediaAdapter() {
        this.oldMediaPlayer = new OldMediaPlayerImplementation();
    }

    @Override
    public void play(String audioType, String filename) {
        if (audioType.equalsIgnoreCase("mp3")) {
            oldMediaPlayer.playMp3(filename);
        } else {
            System.out.println("Formato não suportado: " + audioType);
        }
    }
}