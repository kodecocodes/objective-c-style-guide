/*
 * Some fake Objective-C code to test the uncrustify rules.
 */

@import Foundation;

@implementation FooClass : NSObject

- (NSString *)smilifyString:(NSString *)someString {
  NSString *theString = [someString stringByReplacingOccurrencesOfString:@":)" withString:@":]"];
  return theString;
}

- (NSString *)frownifyString:(NSString *)someString {
  NSString *theString = [someString stringByReplacingOccurrencesOfString:@":(" withString:@":["];
  return theString;
}

- (NSArray *)smilifyStrings:(NSArray *)strings {
  NSMutableArray *workingArray = [NSMutableArray array];
  for (NSString *string in strings) {
    [workingArray addObject:[self smilifyString:string]];
  }

  return [workingArray copy];
}

@end

