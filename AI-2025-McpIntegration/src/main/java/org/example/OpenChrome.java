package org.example;

import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.URL;
import java.nio.charset.StandardCharsets;
import java.util.Scanner;

public class OpenChrome {
    public static void main(String[] args) throws Exception {
        String endpoint = "http://localhost:4444/wd/hub/session";
        String payload = "{\"capabilities\":{\"alwaysMatch\":{\"browserName\":\"chrome\"}}}";

        URL url = new URL(endpoint);
        HttpURLConnection conn = (HttpURLConnection) url.openConnection();
        conn.setRequestMethod("POST");
        conn.setRequestProperty("Content-Type", "application/json");
        conn.setDoOutput(true);

        try (OutputStream os = conn.getOutputStream()) {
            byte[] input = payload.getBytes(StandardCharsets.UTF_8);
            os.write(input, 0, input.length);
        }

        int responseCode = conn.getResponseCode();
        System.out.println("Response Code: " + responseCode);
        String responseBody;
        try (Scanner scanner = new Scanner(conn.getInputStream(), StandardCharsets.UTF_8)) {
            responseBody = scanner.useDelimiter("\\A").next();
            System.out.println("Response Body: " + responseBody);
        }

        // Extract sessionId from response
        String sessionId = null;
        int idIndex = responseBody.indexOf("sessionId");
        if (idIndex != -1) {
            int colonIndex = responseBody.indexOf(':', idIndex);
            int commaIndex = responseBody.indexOf(',', colonIndex);
            if (commaIndex == -1) commaIndex = responseBody.indexOf('}', colonIndex);
            sessionId = responseBody.substring(colonIndex + 2, commaIndex - 1).replaceAll("\"", "");
        }
        if (sessionId == null || sessionId.isEmpty()) {
            System.err.println("Could not extract sessionId");
            return;
        }
        System.out.println("Session ID: " + sessionId);

        // Send POST to /session/{sessionId}/url to navigate to GitHub MCP Selenium page
        String urlEndpoint = "http://localhost:4444/wd/hub/session/" + sessionId + "/url";
        String urlPayload = "{\"url\":\"https://github.com/angiejones/mcp-selenium\"}";
        URL navUrl = new URL(urlEndpoint);
        HttpURLConnection navConn = (HttpURLConnection) navUrl.openConnection();
        navConn.setRequestMethod("POST");
        navConn.setRequestProperty("Content-Type", "application/json");
        navConn.setDoOutput(true);
        try (OutputStream os = navConn.getOutputStream()) {
            byte[] input = urlPayload.getBytes(StandardCharsets.UTF_8);
            os.write(input, 0, input.length);
        }
        int navResponseCode = navConn.getResponseCode();
        System.out.println("Navigate Response Code: " + navResponseCode);
        try (Scanner scanner = new Scanner(navConn.getInputStream(), StandardCharsets.UTF_8)) {
            String navResponseBody = scanner.useDelimiter("\\A").next();
            System.out.println("Navigate Response Body: " + navResponseBody);
        }
    }
}
