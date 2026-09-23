public static String ReverseString(String text) {
    String reversed = "";

    for (int i = text.length() - 1; i >= 0; i--) {
        reversed += text.charAt(i);
    }

    return reversed;
}
