//import com.kikakeyboard.model.nearline.Init;
//import org.springframework.context.ApplicationContext;
import com.kikakeyboard.dataplant.StableRedisPool;
import com.kikakeyboard.dataplant.RedisPool;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.ArrayList;

public class main {
    public void test(){
        System.out.println("66666666666");
    }

    public static void main(String[] args) {
/*
        System.out.println("66666666666");
        Init a =  new Init();
        System.out.println("22222222222");
        ApplicationContext b = a.getConfig();
        System.out.println("333333333:");
*/
        // 9765211813224cf1bf8173181dfa972e
        List<String> a = new ArrayList<String>(){{
            add("b4b7d7cc9454464b938177d412874ce9");
        }};

        Map<String, List<String>> result = RedisPool.getUsersSteps(a, 0, -1);
        //Map<String, List<String>> result = StableRedisPool.getUsersSteps(a, 0, -1);
        //Map<String, List<String>> result = new HashMap<String, List<String>>();
        System.out.println(result);
        for(Map.Entry<String, List<String>> s: result.entrySet()){
            System.out.println(s.getKey() + "  " + s.getValue());
        }
        System.out.println("");
        /*
        */
        // a1be32a10c414065a20e7b755018150c
        Map<String, String> a1 = new HashMap<String, String>(){{

            put("b4b7d7cc9454464b938177d412874ce9", "ok");
        }};

/*
 *
            put("222d9493b3d84a78afd43e66f0b5f23d", "jajaja");
            put("e581be8f62b949bfa7c21ded9aae1a5b", "ok");
            put("c08303790bc74a1c98ac1cbbae2fa7b9", "ok");
            put("85079059edf5416b95d63a96056fc484", "ok");
            put("5d5cbe361f78405ebd3dd4eafcde9645", "ok");
            put("dd4c27e41fd5e3ee5dd7f9eaca5ee466", "ok");
            put("6775876f0060457a86d54e8163fa198b", "ok");
            put("4a5e248cb2554a94ab500e2a09efda3f", "ok");
            put("65a8774cf1d14a6c80a1a9930e578cce", "ok");
            put("255bce527f204e6395e670466867d902", "ok");
            put("982414df46f044dc9c99f77417f2bb96", "ok");
            put("6297312bfe1543769b7b976966183158", "ok");
            put("e4427c705d534479a3988484de63cf7d", "ok");
            put("27ee4af6fbf64889b68503b560120263", "ok");
            put("4f36a8f30add4a8f8da38c29875b99de", "ok");
            put("a393476a0cd2f413dad6c13f82a45368", "ok");
            put("cb8d03f2075d44d9969b43c2bf081d23", "ok");
            put("03fd113a3a7e441b85aede0843f5dc6f", "ok");
            put("1933fc9750a9492c937809722059755a", "ok");
            put("78d5cb82ee4ae36b917bc2996d61315d", "ok");
            put("81930f4038c7426ca50314b2b36fcd04", "ok");
            put("8523a2b956f746cf9e53c108957f66a0", "ok");
            put("45f4e710bf744849888608bd0323bf3b", "ok");
            put("634426ef2ab646cba55fbf9ee7b62532", "ok");
 *
 * */

        //Map<String, Set<String>> result1  = StableRedisPool.getUsersByTag(a1, 0, -1);
        Map<String, Set<String>> result1  = RedisPool.getUsersByTag(a1, 0, -1);
        System.out.println(result1);

    }
}
