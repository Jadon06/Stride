import { Pressable, StyleSheet, Text, View } from 'react-native';
import ThemeBackground from '../components/ThemeBackground';

export default function AuthScreen() {
  return (
    <ThemeBackground>
      <View style={styles.center}>
        <Text style={styles.title}>Stride</Text>

        <Pressable style={({ pressed }) => [styles.primaryBtn, pressed && styles.btnPressed]}>
          <Text style={styles.primaryBtnText}>Sign Up</Text>
        </Pressable>

        <Pressable style={({ pressed }) => [styles.secondaryBtn, pressed && styles.btnPressed]}>
          <Text style={styles.secondaryBtnText}>Log In</Text>
        </Pressable>
      </View>
    </ThemeBackground>
  );
}

const styles = StyleSheet.create({
  center: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
    paddingHorizontal: 32,
  },
  title: {
    fontFamily: 'Lora_700Bold_Italic',
    fontSize: 72,
    color: '#E87040',
    letterSpacing: -1.6,
    lineHeight: 80,
    marginBottom: 36,
  },
  primaryBtn: {
    width: 180,
    backgroundColor: 'transparent',
    paddingVertical: 14,
    borderRadius: 999,
    alignItems: 'center',
    borderWidth: 1.5,
    borderColor: '#E87040',
    marginBottom: 12,
  },
  primaryBtnText: {
    fontFamily: 'Lora_700Bold_Italic',
    fontSize: 20,
    color: '#E87040',
  },
  secondaryBtn: {
    width: 180,
    backgroundColor: 'transparent',
    paddingVertical: 14,
    borderRadius: 999,
    alignItems: 'center',
    borderWidth: 1.5,
    borderColor: '#E87040',
  },
  secondaryBtnText: {
    fontFamily: 'Lora_700Bold_Italic',
    fontSize: 20,
    color: '#E87040',
  },
  btnPressed: {
    opacity: 0.8,
    transform: [{ scale: 0.98 }],
  },
});
