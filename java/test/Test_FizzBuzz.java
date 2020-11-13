import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class Test_FizzBuzz {

    @Test
    public void testFizzBuzzNumber() {
        String result = FizzBuzz.fizzBuzz(2);
        assertEquals(result,"2")
    }
}
