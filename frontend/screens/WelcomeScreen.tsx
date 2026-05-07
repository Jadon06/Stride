import { useEffect, useRef } from 'react';
import { Animated, StyleSheet, View } from 'react-native';
import ThemeBackground from '../components/ThemeBackground';

type Props = { onComplete: () => void };

export default function WelcomeScreen({ onComplete }: Props) {
  const opacity = useRef(new Animated.Value(0)).current;

  useEffect(() => {
    Animated.timing(opacity, {
      toValue: 1,
      duration: 700,
      useNativeDriver: true,
    }).start();

    const timer = setTimeout(() => {
      Animated.timing(opacity, {
        toValue: 0,
        duration: 500,
        useNativeDriver: true,
      }).start(() => onComplete());
    }, 2500);

    return () => clearTimeout(timer);
  }, []);

  return (
    <ThemeBackground>
      <View style={styles.center}>
        <Animated.View style={{ opacity, alignItems: 'center' }}>
          <Animated.Text style={styles.title}>Stride</Animated.Text>
          <Animated.Text style={styles.tagline}>a digital fitness partner</Animated.Text>
        </Animated.View>
      </View>
    </ThemeBackground>
  );
}

const styles = StyleSheet.create({
  center: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
  },
  title: {
    fontFamily: 'Lora_700Bold_Italic',
    fontSize: 84,
    color: '#E87040',
    letterSpacing: -2,
    lineHeight: 92,
  },
  tagline: {
    fontFamily: 'Lora_400Regular',
    fontSize: 18,
    color: '#7A5A40',
    marginTop: 6,
    letterSpacing: 0.2,
  },
});
