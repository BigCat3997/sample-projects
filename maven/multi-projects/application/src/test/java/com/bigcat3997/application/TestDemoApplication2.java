package com.bigcat3997.application;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

public class TestDemoApplication2 {

	@Test
	public void testAdd() {
		assertEquals(20, Integer.sum(10, 10));
	}
}
