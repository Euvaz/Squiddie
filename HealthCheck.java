import java.io.IOException;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse.BodyHandlers;

public class HealthCheck {

  public static void main(String[] args) throws InterruptedException, IOException {
    var client = HttpClient.newHttpClient();
    var request = HttpRequest.newBuilder()
        .uri(URI.create("http://localhost:2333/metrics"))
        .build();

    var response = client.send(request, BodyHandlers.ofString());

    if (response.statusCode() != 200) {
      throw new RuntimeException("Healthcheck failed");
    }
  }
}
