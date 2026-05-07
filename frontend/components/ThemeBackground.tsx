import { ReactNode } from 'react';
import { StyleSheet, View } from 'react-native';
import { LinearGradient } from 'expo-linear-gradient';

type Props = { children?: ReactNode };

export default function ThemeBackground({ children }: Props) {
  return (
    <View style={styles.root}>
      <LinearGradient
        colors={['rgba(255,200,150,0.5)', 'rgba(255,200,150,0)']}
        start={{ x: 0, y: 0 }}
        end={{ x: 1, y: 1 }}
        style={StyleSheet.absoluteFill}
      />
      <LinearGradient
        colors={['rgba(180,160,220,0)', 'rgba(180,160,220,0.25)']}
        start={{ x: 0, y: 0 }}
        end={{ x: 1, y: 1 }}
        style={StyleSheet.absoluteFill}
      />
      {children}
    </View>
  );
}

const styles = StyleSheet.create({
  root: {
    flex: 1,
    backgroundColor: '#DDD5C8',
  },
});
