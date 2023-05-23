package waterpoweredappHAR;

import java.time.Duration;
import java.util.*;

import io.gatling.javaapi.core.*;
import io.gatling.javaapi.http.*;
import io.gatling.javaapi.jdbc.*;

import static io.gatling.javaapi.core.CoreDsl.*;
import static io.gatling.javaapi.http.HttpDsl.*;
import static io.gatling.javaapi.jdbc.JdbcDsl.*;

public class RecordedSimulation extends Simulation {

  private HttpProtocolBuilder httpProtocol = http
    .baseUrl("http://127.0.0.1:30000")
    .inferHtmlResources()
    .acceptHeader("image/avif,image/webp,*/*")
    .acceptEncodingHeader("gzip, deflate, br")
    .acceptLanguageHeader("en-US,en;q=0.5")
    .userAgentHeader("Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/112.0");
  
  private Map<CharSequence, String> headers_0 = Map.ofEntries(
    Map.entry("Accept", "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8"),
    Map.entry("Sec-Fetch-Dest", "document"),
    Map.entry("Sec-Fetch-Mode", "navigate"),
    Map.entry("Sec-Fetch-Site", "same-origin"),
    Map.entry("Sec-Fetch-User", "?1"),
    Map.entry("Upgrade-Insecure-Requests", "1")
  );
  
  private Map<CharSequence, String> headers_1 = Map.ofEntries(
    Map.entry("Sec-Fetch-Dest", "image"),
    Map.entry("Sec-Fetch-Mode", "no-cors"),
    Map.entry("Sec-Fetch-Site", "same-origin")
  );


  private ScenarioBuilder scn = scenario("RecordedSimulation")
    .exec(
      http("RecordedSimulation_0")
        .get("/")
        .headers(headers_0)
        .resources(
          http("RecordedSimulation_1")
            .get("/favicon.ico")
            .headers(headers_1)
            .check(status().is(404))
        )
    )
    .pause(9)
    .exec(
      http("RecordedSimulation_2")
        .get("/store")
        .headers(headers_0)
        .resources(
          http("RecordedSimulation_3")
            .get("/favicon.ico")
            .headers(headers_1)
            .check(status().is(404))
        )
    )
    .pause(13)
    .exec(
      http("RecordedSimulation_4")
        .get("/profile")
        .headers(headers_0)
        .resources(
          http("RecordedSimulation_5")
            .get("/favicon.ico")
            .headers(headers_1)
            .check(status().is(404))
        )
    )
    .pause(5)
    .exec(
      http("RecordedSimulation_6")
        .get("/recommendations")
        .headers(headers_0)
        .resources(
          http("RecordedSimulation_7")
            .get("/favicon.ico")
            .headers(headers_1)
            .check(status().is(404))
        )
    )
    .pause(8)
    .exec(
      http("RecordedSimulation_8")
        .get("/logout")
        .headers(headers_0)
        .resources(
          http("RecordedSimulation_9")
            .get("/favicon.ico")
            .headers(headers_1)
            .check(status().is(404))
        )
    );

  {
	  setUp(scn.injectOpen(rampUsers(100).during(60))).protocols(httpProtocol);
  }
}
