
public class OldMediaPlayerImplementation implements OldMediaPlayerInterface {
    @Override
    public void playMp3(String filename) {
        System.out.println("Tocando arquivo MP3: " + filename);
    }
}